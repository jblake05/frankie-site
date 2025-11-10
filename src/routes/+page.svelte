<script>
    import Image from "$lib/components/Image.svelte";
    // access all images in directory, put in an array, pick a random (10-20) amount of photos from the entire directory
    const imageModules = import.meta.glob("../lib/assets/ravelry/*.{png,jpeg,jpg}", {
        eager: true,
        query: '?url', 
        import: 'default'
    });

    const imageUrls = Object.values(imageModules);
    // .slice(0,  50);
    
    let index = 0;

    const indices = [0, 1, 2, 3];
</script>

<style>
    h1 {
        text-align: center;
    }

    .navbar {
        text-align: center;
        border: 1px solid;
    }

    .navbar a {
        padding-left: 5%;
        padding-right: 5%;
        font-size: larger;
    }

    .flex-container {
        display: flex;
        width: 100%;
        flex-wrap: wrap;
        /* align-content: flex-start; */
        align-content: stretch;
        justify-content: space-evenly;

    }

    .page {
        background-color: brown;
        /* width: 100%;
        height: 100%; */
        /* height: 100vh; */
    }

</style>

    <div class="navbar">
        <a href="./knitting">knitting</a>
        <a href="./music">music</a>
        <a href="./spinning">spinning</a>
        <a href="./misc">misc</a>
    </div>

<div class="page">
    <h1> FRANKIES WORLD </h1>

    <div class="welcome" style="text-align: center;">
        <h2>welcome text</h2>
    </div>

    <!-- <Image src="src/lib/assets/ravelry/poppop_dagrun_luggar.jpg" alt="test"></Image> -->
    {#each indices as index} 
    <!-- just repeating this pattern for background texture -->
    <div class="flex-container">
    {#each imageUrls as imageUrl}
        <Image src={imageUrl} alt="Test"></Image>
    {/each}
    </div>
    {/each}
</div>