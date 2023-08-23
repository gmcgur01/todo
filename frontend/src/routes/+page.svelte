<script>
    import { getCookie } from "./+server";

    let text = "";

    async function handleClick () {
        let body = new FormData();
        body.append("title", "Finish todo app");

        let res = await fetch("/api/1/add-task/", {
            method : "POST",
            headers: {
                'X-CSRFToken': getCookie("csrftoken"),
            },
            body : body
        })
        text = String(res.status)
    }

</script>

<button on:click={handleClick}>
    Send task!
</button>


{#if text}
    {text}
{/if}

<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
