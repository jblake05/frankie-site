<script>
    import Page from "../../routes/+page.svelte";

    let {data, cwd} = $props();
    // import { data } from "$lib/components/data.js"

    let setBrightness = (id, brightness) => {
        document.getElementById(id).style.filter = `brightness(${brightness}%)`
    };

    const knittingModules = import.meta.glob("$lib/assets/ravelry/*.{png,jpeg,jpg}", {
            eager: true,
            import: 'default'
        });
    const otherModules = import.meta.glob("$lib/assets/*.{png,jpeg,jpg}", {
            eager: true,
            import: 'default'
        });

    // const path = `/src/lib/assets/ravelry/${srcInfo[0]}.${srcInfo[1]}`;


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
    <!-- do an image glob here too . . . . and send that glob as a parameter to the entry / slug page ideally!!! -->

    <!-- {#each imageUrls as imageUrl}
        <img src={imageUrl} alt="Test"/>
    {/each} -->


    {#each data.summaries as {slug, title, src}}
        <div class="cell" id={title} style="filter: brightness(100%);" onmouseenter={()=> {
            setBrightness(title, 50);
        }}
        onmouseleave={()=>{
            setBrightness(title, 100);
        }}>            
        <!-- todo: make this routing dynamic depending on subfolder -->
        <!-- use enhanced:img here and pass as a param like in Entry/(knitting/[slug])? -->
        {#if cwd ==="knitting"}
            <a href="./{cwd}/{slug}"><img src={knittingModules[`/src/lib/assets/ravelry/${src.split(".")[0]}.${src.split(".")[1]}`]} alt="test"/></a>
        {:else}
            <a href="./{cwd}/{slug}"><img src={otherModules[`/src/lib/assets/${src.split(".")[0]}.${src.split(".")[1]}`]} alt="test"/></a>
        {/if}
        <br>
            {title}
        </div>
    {/each}
</div>