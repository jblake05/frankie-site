<script>
    let { data, cwd } = $props();

    // const imageRightAlign = Math.random() > 0.5;
    const imageAlign = Math.random() > 0.5;
    function r(start, end) {
        return (Math.random() * (end - start)) + start;
    }
    const h = r(0, 360);
    const s = r(35, 100);
    const v = r(50, 75);

    const mainColor = `hsl(${h}deg ${s}% ${v}%);`;
    const complementaryColor = `hsl(${(h + 180) % 360}deg ${s}% ${v}%);`;
</script>

<style>

    .image-container {
        width: 33%;
        height: 100%;
        /* padding-left: 5%; */
        /* text-align: left; */
    }

    .imageLeftAlign {
        margin-right: auto;
        padding-left: 5%;    
    }

    .imageRightAlign {
        margin-left: auto;
        padding-right: 5%;
    }

    h1 {
        text-align: center;
    }

</style>

<!-- has slug, title, img_src -- needs desc? -->
<div style={`height: 100vh; background-color:${mainColor};`}>
 <h1>{data.post.title}</h1>

 <div class={["image-container", (imageAlign? "imageRightAlign": "imageLeftAlign")]}>
    {#if cwd==="knitting"}
        <img src="../src/lib/assets/ravelry/{data.post.src}" style={`border: solid ${r(3, 10)}px ${complementaryColor};`} alt="Placeholder"/>
    {:else}
        <img src="../src/lib/assets/{data.post.src}" style={`border: solid ${r(3, 10)}px ${complementaryColor};`} alt="Placeholder"/>
    {/if}
 </div>

<p>
    {data.post.description}
</p>
</div>