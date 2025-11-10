
<script>
    let {data} = $props();

    import Grid from "$lib/components/Grid.svelte";
</script>
<style>

.inner {
    width: 100%;
    background-color: blueviolet;
}
</style>

<div class="inner">
<h1>knitting</h1>

<!-- definitely a better way to do this other than cwd as a prop -->
<Grid data={data} cwd="knitting"></Grid>
</div>