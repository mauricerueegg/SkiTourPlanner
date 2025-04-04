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
			const res = await fetch('http://localhost:5000/api/predict', {
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

<style>
	form {
		max-width: 500px;
		margin: auto;
		padding: 2rem;
		background: #fff;
		border-radius: 1rem;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	}

	label {
		display: block;
		margin-top: 1rem;
		font-weight: bold;
	}

	input {
		width: 100%;
		padding: 0.5rem;
		margin-top: 0.3rem;
	}

	button {
		margin-top: 2rem;
		padding: 0.8rem 1.5rem;
		background-color: #007bff;
		color: white;
		border: none;
		border-radius: 0.5rem;
		cursor: pointer;
	}

	button:hover {
		background-color: #0056b3;
	}

	.result, .error {
		text-align: center;
		margin-top: 2rem;
		font-size: 1.2rem;
	}

	.error {
		color: red;
	}
</style>

<form on:submit|preventDefault={predict}>
	<h2>Lawinenrisiko Vorhersage</h2>

	<label for="hoehe">Höhendifferenz (m)</label>
	<input id="hoehe" type="number" bind:value={hoehe} required />

	<label for="route">Routenlänge (m)</label>
	<input id="route" type="number" bind:value={route} required />

	<label for="schnee">Schnee (cm)</label>
	<input id="schnee" type="number" bind:value={schnee} required />

	<label for="gipfel">Gipfelhöhe (m)</label>
	<input id="gipfel" type="number" bind:value={gipfel} required />

	<button type="submit" disabled={loading}>
		{loading ? 'Berechne...' : 'Vorhersagen'}
	</button>

	{#if risiko !== null}
		<div class="result">Vorhergesagtes Risiko: {risiko.toFixed(2)}</div>
	{/if}

	{#if error}
		<div class="error">{error}</div>
	{/if}
</form>
