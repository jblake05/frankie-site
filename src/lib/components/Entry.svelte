<script>
    // the way to go about this is, in your given display grid, you get the import 
    let { image, title, description } = $props();

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

    /* DESKTOP CSS */
    @media only screen and (min-width: 600px) {
        .image-container {
            width: 33%;
        }

        .imageLeftAlign {
            order: 0;
            margin-right: auto;
            padding-left: 15%;    
        }

        .imageRightAlign { /* fix styling here */
            order: 1;
            margin-left: auto;
            padding-right: 15%;
        }

        .text-container {
            width: 33%;
        }

        .textLeftAlign {
            order: 0;
            margin-right: auto;
            padding-left: 15%;
        }

        .textRightAlign {
            order: 1;
            margin-left: auto;
            padding-right: 15%;
        }

        .page-container {
            display: flex;
            align-items: center;
        }
    }

    /* MOBILE CSS */
    @media only screen and (max-width: 600px) {
        .image-container {
            width: 25%;
            height: auto;
        }

        .imageLeftAlign {
            float: left;
        }

        .imageRightAlign { /* fix styling here */
            float: right;
        }

        .text-container {
            width: 10%;
        }

        .textLeftAlign {
            float: left;
        }

        .textRightAlign {
            float: right;
        }

        img{
            width: 10%;
        }

        h1 {
            font-size: 1px;
        }
        
    }

    h1 {
        text-align: center;
    }

    .page-container {
        width: 100%;
    }

</style>

<!-- has slug, title, img_src -- needs desc? -->
<div style={`height: 100vh; background-color:${mainColor};`}>
  <h1>{title}</h1>
<div class="page-container" >

 <div class={["image-container", (imageAlign? "imageRightAlign": "imageLeftAlign")]}>
    <img src={image} style={`border: solid ${r(3, 10)}px ${complementaryColor};`} alt="Placeholder"/>
 </div>

    <div class={["text-container", (imageAlign? "textLeftAlign" : "textRightAlign")]}>
        {description}
    </div>

</div>
</div>