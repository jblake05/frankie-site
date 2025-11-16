<script>
    import Entry from "$lib/components/Entry.svelte";
    
    let {data} = $props();

    const images = import.meta.glob("$lib/assets/*.{png,jpeg,jpg}", {
        eager: true,
        import: 'default'
    });

    const title = data.post.title;
    const description = data.post.description;

    const srcInfo = data.post.src.split(".");
    const path = `/src/lib/assets/${srcInfo[0]}.${srcInfo[1]}`;
    
</script>
<!-- description and image of proj -->
<Entry image={images[path]} title={title} description={description}> </Entry>