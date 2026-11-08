<template>
  <ForestBackground class="page-background" />

  <PageLayout title="Accueil">
    <p>En construction.</p>
  </PageLayout>
</template>

<script lang="ts">
import ForestBackground from '@/components/forest/ForestBackground.vue'
import PageLayout from '@/components/PageLayout.vue'

export default {
  name: 'HomeView',
  components: {
    ForestBackground,
    PageLayout,
  },
}
</script>

<style scoped>
.page-background {
  position: fixed;
  inset: 0;
  z-index: -1;
}
</style>
