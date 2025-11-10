<script>
    let {src, altText} = $props();
    // console.log(data);
    // console.log(styling);
    function r(start, end) {
        return (Math.random() * (end - start)) + start;
    }
</script>

<style>
    img {
        align-self: center;
        display: inline-flex;
        height: auto;
    }
</style>
<!-- height: ${r(50, 500)}px; --> 
 <!-- goal: make image particles -->
<img src={src} style={`width: ${r(5, 50)}px; margin-left: ${r(-50, 50)}px; opacity: ${r(0.25, 0.75)}; filter:brightness(${r(50, 150)}%); border:solid ${r(1, 10)}px rgb(${r(0, 255)}, ${r(0, 255)}, ${r(0, 255)}); z-index:${r(-50, -1)};`} alt={altText}/>