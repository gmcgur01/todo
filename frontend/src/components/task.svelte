<script lang="ts">
    import { getCookie } from "../cookie";
    import { createEventDispatcher } from 'svelte';

	export let userId: string;
    export let title: string;
    export let taskId: string;
    export let index: number;

    console.log("title:", title);
    console.log("index:", index);

	const dispatch = createEventDispatcher();

    async function addTask () {
        let newTitle = (document.getElementsByClassName('textInput')[0] as HTMLInputElement).value;
        if (newTitle === "") {
            return;
        }

        let body = new FormData();
        body.append("title", newTitle);

        let res = await fetch("/api/" + userId + "/add-task/", {
            method : "POST",
            headers: {
                'X-CSRFToken': getCookie("csrftoken"),
            },
            body : body
        })

        if (res.status == 200) {
            taskId = await res.text();
        } else {
            console.error("Error posting new task");
        }

        dispatch("addNew", {
            index: index,
            title: newTitle,
            taskId: taskId
        });
    }

    async function deleteTask () {
        let res = await fetch("/api/delete-task/" + taskId + "/", {
            method: "DELETE",
            headers: {
                'X-CSRFToken': getCookie("csrftoken"),
            }
        })

        if (res.status != 200) {
            console.error("Error deleting task");
        }

        dispatch("deleteTask", {
            index: index
        })
    }

</script>

<div class="paper">

    {#if title !== ""}
        <h3>
            {title}
        </h3>
        <button on:click={deleteTask}>
            <svg fill="none" viewBox="0 0 24 24" height="24" width="24" xmlns="http://www.w3.org/2000/svg">
                <path xmlns="http://www.w3.org/2000/svg" d="M20.6644 5.2526C21.0772 5.61952 21.1143 6.25159 20.7474 6.66437L10.0808 18.6644C9.89099 18.8779 9.61898 19 9.33334 19C9.04771 19 8.7757 18.8779 8.58593 18.6644L3.2526 12.6644C2.88568 12.2516 2.92286 11.6195 3.33565 11.2526C3.74843 10.8857 4.3805 10.9229 4.74742 11.3356L9.33334 16.4948L19.2526 5.33565C19.6195 4.92286 20.2516 4.88568 20.6644 5.2526Z" fill="#0D0D0D"></path>
            </svg>
        </button>
    {:else}
        <input type="text" class="textInput" maxlength="200">
        <button on:click={addTask}>
            <svg fill="none" viewBox="0 0 24 24" height="24" width="24" xmlns="http://www.w3.org/2000/svg">
                <path xmlns="http://www.w3.org/2000/svg" d="M12 4C12.5523 4 13 4.44772 13 5V11H19C19.5523 11 20 11.4477 20 12C20 12.5523 19.5523 13 19 13H13V19C13 19.5523 12.5523 20 12 20C11.4477 20 11 19.5523 11 19V13H5C4.44772 13 4 12.5523 4 12C4 11.4477 4.44772 11 5 11H11V5C11 4.44772 11.4477 4 12 4Z" fill="#0D0D0D"></path>
            </svg>
        </button>
    {/if}
</div>

<style>
    .paper {
        display: flex;
        padding: 10px;
        outline: 5px solid seagreen;
        overflow: auto;
        width: 500px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 13px;
        border-radius: 3px;
        background-color: whitesmoke;
        word-wrap: break-word;
    }

    h3 {
        margin-top: auto;
        margin-bottom: auto;
        font-weight: 100;
        color: black;
        overflow: auto;
    }

    button {
        margin-left: auto;
        margin-bottom: auto;
        padding: 5px;
        border: none;
        background-color: whitesmoke;
    }

    button:hover {
        background-color: #e6e6e6;
    }

    input {
        outline: none;
        border: none;
        border-bottom: 1px solid black;
        width: 100%;
        background-color: whitesmoke;
        font-size: 18px;
        word-wrap: break-word;
    }
    
</style>

