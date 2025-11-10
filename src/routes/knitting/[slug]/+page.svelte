<script>
    import Entry from "$lib/components/Entry.svelte";
    
    let {data} = $props();

</script>
<!-- description and image of proj -->
<Entry data={data} cwd="knitting"> </Entry>