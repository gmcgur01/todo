<script>
    import { setCookie, getCookie } from "./+server";
    import { onMount } from "svelte";

    let text = "";

    onMount(async () => {
        let userId = getCookie("userId");
        if (userId === null) {
            const res = await fetch("/api/new-user/");
            if (res.status === 200) {
                userId = await res.text();
            } else {
                console.error("Error getting new user.");
                userId = "No ID found!";
            }
        }
        text = userId;
    });


    async function handleClick () {
        setCookie("userId", "1", 1);
        // let body = new FormData();
        // body.append("title", "Finish todo app");

        // let res = await fetch("/api/1/add-task/", {
        //     method : "POST",
        //     headers: {
        //         'X-CSRFToken': getCookie("csrftoken"),
        //     },
        //     body : body
        // })
        // text = String(res.status)
    }

</script>

<button on:click={handleClick}>
    Send task!
</button>


{#if text}
    {text}
{/if}

<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
