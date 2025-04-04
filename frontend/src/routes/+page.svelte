<script>
    let input = {
        Höhendifferenz: 1000,
        Routenlänge: 2000,
        Schnee: 2000.0,
        Gipfelhöhe: 3000,
        Schwierigkeitsgrad_num: 3.0
    };
    let prediction = null;
    let error = null;

    async function predict() {
        try {
            error = null;
            const response = await fetch("http://127.0.0.1:5000/api/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(input)
            });

            if (!response.ok) {
                throw new Error(await response.text());
            }

            const data = await response.json();
            prediction = data.lawinenrisiko;
        } catch (err) {
            error = err.message;
        }
    }
</script>

<main>
    <h1>Lawinenrisiko Vorhersage</h1>

    <form on:submit|preventDefault={predict}>
        <label>
            Höhendifferenz:
            <input type="number" bind:value={input.Höhendifferenz} />
        </label>
        <label>
            Routenlänge:
            <input type="number" bind:value={input.Routenlänge} />
        </label>
        <label>
            Schnee:
            <input type="number" step="0.1" bind:value={input.Schnee} />
        </label>
        <label>
            Gipfelhöhe:
            <input type="number" bind:value={input.Gipfelhöhe} />
        </label>
        <label>
            Schwierigkeitsgrad (numerisch):
            <input type="number" step="0.1" bind:value={input.Schwierigkeitsgrad_num} />
        </label>
        <button type="submit">Vorhersagen</button>
    </form>

    {#if prediction !== null}
        <p>Vorhergesagtes Lawinenrisiko: {prediction}</p>
    {/if}

    {#if error}
        <p style="color: red;">Fehler: {error}</p>
    {/if}
</main>