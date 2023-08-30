<script lang="ts">
    import '../styles.css';
    import Task from '../components/task.svelte'
    import { getCsrfToken, setCookie, getCookie } from "../cookie";
    import { onMount } from "svelte";

    let userId = "";

    onMount(async () => {
        getCsrfToken();
        userId = getCookie("userId");
        if (userId === null) {
            const res = await fetch("/api/new-user/");
            if (res.status === 200) {
                userId = await res.text();
                setCookie("userId", userId, 7);
            } else {
                console.error("Error getting new user.");
                userId = "-1";
            }
        }
        getTasks();
    });

    let tasks: { taskId: string; title: string; }[] = [];

    async function getTasks () {
        const res = await fetch("/api/" + userId + "/tasks/");
        if (res.status === 200) {
            tasks = await res.json();
            for (let task of tasks) {
                console.log(task);
            }
            tasks.push({taskId: "", title: ""});
        } else {
            console.error("Error getting tasks.");
        }
    }

    function addNew(event: any) {
        tasks[event.detail.index] = {taskId: event.detail.taskId, title: event.detail.title};
        tasks = [...tasks, {taskId: "", title: ""}];
    }

    function deleteTask(event: any) {
        tasks.splice(event.detail.index, 1);
        tasks = tasks;
    }
    

</script>

<div id="topBar">
    <h1 id="title"> todo </h1>
</div>

<div id="taskList">
    {#each tasks as task, i}
        <Task 
            taskId={task.taskId} 
            title={task.title} 
            userId={userId} 
            index={i} 
            on:addNew={addNew} 
            on:deleteTask={deleteTask}
        />
    {/each}
</div>


<style>
    #topBar {
        position: sticky;
        top: 0px;
        z-index: 100;
        background-color: whitesmoke;
    }
    #title {
        color: SeaGreen;
        text-align: center;
        font-size: 50px;
    }   
    #taskList {
        overflow: auto;
        height: auto;
    }
</style>
