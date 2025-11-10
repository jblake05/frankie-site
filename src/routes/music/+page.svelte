<script>
    let {data} = $props();
    import Grid from "$lib/components/Grid.svelte";
</script>

<h1>music</h1>
<Grid data={data} cwd="music"></Grid>