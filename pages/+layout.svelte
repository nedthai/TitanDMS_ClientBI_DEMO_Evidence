<script>
  import "@evidence-dev/tailwind/fonts.css";
  import "../app.css";
  import { EvidenceDefaultLayout } from "@evidence-dev/core-components";
  export let data;
</script>

<style>
  /* Zero out the sidebar offset globally */
  :global(:root) {
    --sidebar-width: 0px !important;
  }

  /* Force the aside/sidebar out of layout flow entirely.
     hideSidebar={true} adds 'hidden' but Evidence's q:block overrides it. */
  :global(aside) {
    display: none !important;
    width: 0 !important;
    max-width: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    overflow: hidden !important;
  }

  /* Prevent horizontal overflow from internal wrappers */
  :global(html),
  :global(body) {
    overflow-x: hidden;
    max-width: 100vw;
  }

  /* Reset Evidence's main content wrapper */
  :global(main) {
    margin-left: auto !important;
    margin-right: auto !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    width: 100% !important;
    max-width: 100vw !important;
    box-sizing: border-box !important;
  }

  /* Center the inner content container */
  .centered-container {
    max-width: 90rem;
    margin-left: auto;
    margin-right: auto;
    width: 100%;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
    box-sizing: border-box;
  }

  @media (min-width: 768px) {
    .centered-container {
      padding-left: 3rem;
      padding-right: 3rem;
    }
  }

  @media (min-width: 1024px) {
    .centered-container {
      padding-left: 6rem;
      padding-right: 6rem;
    }
  }
</style>

<EvidenceDefaultLayout
  {data}
  hideSidebar={true}
  hideBreadcrumbs={true}
  fullWidth={true}
>
  <div slot="content" class="centered-container">
    <slot />
  </div>
</EvidenceDefaultLayout>
