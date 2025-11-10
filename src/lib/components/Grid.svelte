<script>
    let {data, cwd} = $props();
    // import { data } from "$lib/components/data.js"

    let images = [];
    const ROW_SIZE = 3;
    const COL_SIZE = 3;

    let setBrightness = (id, brightness) => {
        document.getElementById(id).style.filter = `brightness(${brightness}%)`
    };
</script>

<style>
    .grid {
        width: 100%;
        display: flex;
        align-content: stretch;
        flex-wrap: wrap;
        /* display: grid;
        width: 100%;
        grid-template-columns: repeat(6, 15%);
        align-items: center; */
        /* grid-auto-rows: 200px;
        grid-auto-columns: 200px; */
        /* width: 100%; */
    }

    .grid img {
        border: 3px solid;
    }

    .cell {
        text-align: center;
        flex: 1;
    }
</style>

<div class="grid">
    <!-- svelte-ignore a11y_no_static_element_interactions --> 
    
    {#each data.summaries as {slug, title, src}}
        <div class="cell" id={title} style="filter: brightness(100%);" onmouseenter={()=> {
            setBrightness(title, 50);
        }}
        onmouseleave={()=>{
            setBrightness(title, 100);
        }}>            
        <!-- todo: make this routing dynamic depending on subfolder -->
        {#if cwd==="knitting"}
            <a href="./{cwd}/{slug}"><img src="src/lib/assets/ravelry/{src}" alt="test"/></a>
        {:else}
            <a href="./{cwd}/{slug}"><img src="src/lib/assets/{src}" alt="test"/></a>
        {/if}
        <br>
            {title}
        
        </div>
    {/each}
</div>