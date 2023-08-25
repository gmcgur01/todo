<script>
    import '../styles.css';
    import Task from '../components/task.svelte'
    import { setCookie, getCookie } from "./+server";
    import { onMount } from "svelte";

    let text = "";

    onMount(async () => {
        let userId = getCookie("userId");
        if (userId === null) {
            const res = await fetch("/api/new-user/");
            if (res.status === 200) {
                userId = await res.text();
                setCookie("userId", userId, 7);
            } else {
                console.error("Error getting new user.");
                userId = "No ID found!";
            }
        }
        text = userId;
    });


    async function handleClick () {
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

<div>
    <h1> todo </h1>
</div>

<Task userId=userId title="hello world"/>
<Task userId=userId title="This is the thing I need to do!!! It needs to get done!!! This is supposed to get really long so I can test the feature!!!"/>
<Task userId=userId title=""/>

<button on:click={handleClick}>
    Send task!
</button>


{#if text}
    {text}
{/if}

<style>
    h1 {
        color: SeaGreen;
        text-align: center;
        font-size: 50px;
    }   
</style>
