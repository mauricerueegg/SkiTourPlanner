<script lang="ts">
	let hoehe = 1000;
	let route = 2000;
	let schnee = 200;
	let gipfel = 3000;
	let risiko: number | null = null;
	let error: string | null = null;
	let loading = false;

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

<!-- Bootstrap Styling -->
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
						<div class="alert alert-success mt-4 text-center">
							Vorhergesagtes Risiko: {risiko.toFixed(2)}
						</div>
					{/if}
					{#if error}
						<div class="alert alert-danger mt-4 text-center">
							{error}
						</div>
					{/if}
				</div>
			</div>
		</div>
	</div>
</div>