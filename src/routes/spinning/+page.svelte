<script>
    let {data} = $props();
    import Grid from "$lib/components/Grid.svelte";
</script>

<h1>spinning</h1>
<img src="/evil.png" alt="homer"/>
<Grid data={data} cwd="spinning"></Grid>