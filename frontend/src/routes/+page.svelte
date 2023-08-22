<script>

    let text = "";

    async function handleClick () {
        let res = await fetch("/api");
        text = await res.text()
    }


</script>

<button on:click={handleClick}>
    Say hi!
</button>

{#if text}
    {text}
{/if}

<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
