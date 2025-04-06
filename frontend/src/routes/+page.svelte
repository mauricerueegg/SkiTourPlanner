<script lang="ts">
	let hoehe: number | null = null;
	let route: number | null = null;
	let schnee: number | null = null;
	let gipfel: number | null = null;

	let risiko: number | null = null;
	let error: string | null = null;
	let loading = false;

	function risikoFarbe(r: number): string {
		if (r < 1) return 'text-success';
		if (r < 2) return 'text-warning';
		return 'text-danger';
	}

	function risikoIcon(r: number): string {
		if (r < 1) return '🟢';
		if (r < 2) return '🟠';
		return '🔴';
	}

	function risikoText(r: number): string {
		if (r < 1) return 'Tiefes Risiko (0–1)';
		if (r < 2) return 'Erhöhtes Risiko (1–2)';
		return 'Hohes Risiko (2–3)';
	}

	async function predict() {
		loading = true;
		error = null;
		risiko = null;

		try {
			const res = await fetch('/api/predict', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({
					Höhendifferenz: hoehe,
					Routenlänge: route,
					Schnee: schnee,
					Gipfelhöhe: gipfel
				})
			});
			const data = await res.json();
			if (data.error) {
				error = data.error;
			} else {
				risiko = data.lawinenrisiko;
			}
		} catch (e) {
			error = 'Server nicht erreichbar oder ungültige Antwort.';
		} finally {
			loading = false;
		}
	}
</script>

<!-- Bootstrap -->
<link
	href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
	rel="stylesheet"
/>

<div class="container py-5">
	<div class="row justify-content-center">
		<div class="col-md-6">
			<div class="card shadow">
				<div class="card-body">
					<h3 class="card-title mb-4 text-center">Lawinenrisiko Vorhersage</h3>

					<form on:submit|preventDefault={predict}>
						<div class="mb-3">
							<label for="hoehe" class="form-label">Höhendifferenz (m)</label>
							<input id="hoehe" type="number" bind:value={hoehe} required class="form-control" />
						</div>
						<div class="mb-3">
							<label for="route" class="form-label">Routenlänge (m)</label>
							<input id="route" type="number" bind:value={route} required class="form-control" />
						</div>
						<div class="mb-3">
							<label for="schnee" class="form-label">Schnee (cm)</label>
							<input id="schnee" type="number" bind:value={schnee} required class="form-control" />
						</div>
						<div class="mb-3">
							<label for="gipfel" class="form-label">Gipfelhöhe (m)</label>
							<input id="gipfel" type="number" bind:value={gipfel} required class="form-control" />
						</div>

						<button type="submit" class="btn btn-primary w-100" disabled={loading}>
							{loading ? 'Berechne...' : 'Vorhersagen'}
						</button>
					</form>

					{#if risiko !== null}
						<div class="mt-4 text-center">
							<p class={`fs-5 fw-bold ${risikoFarbe(risiko)}`} title={risikoText(risiko)}>
								{risikoIcon(risiko)} {risikoText(risiko)} – {risiko.toFixed(2)}
							</p>
						</div>
					{/if}

					{#if error}
						<div class="alert alert-danger mt-4 text-center">
							{error}
						</div>
					{/if}
				</div>
			</div>

			<!-- Infobox -->
			<div class="mt-4">
				<h5>Was bedeuten die drei Risikokategorien?</h5>
				<ol class="small">
					<li><span class="text-success fw-bold">🟢 Tiefes Risiko (0–1):</span> Relativ sicher, wenn keine speziellen Gefahrenzeichen vorliegen. Auch grüne Routen weisen ein Restrisiko auf.</li>
					<li><span class="text-warning fw-bold">🟠 Erhöhtes Risiko (1–2):</span> Nur für erfahrene Tourengänger:innen geeignet. Die Situation muss umfassend analysiert werden.</li>
					<li><span class="text-danger fw-bold">🔴 Hohes Risiko (2–3):</span> Von Skitouren mit diesem Risiko ist dringend abzuraten.</li>
				</ol>
				<p class="text-muted small">
					Der Wert zwischen 0 und 3 zeigt an, wie nah eine Route an der Grenze zur nächsten Kategorie liegt.
				</p>
			</div>
		</div>
	</div>
</div>