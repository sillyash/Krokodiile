<template>
  <div class="forest" aria-hidden="true">
    <!-- Separate from the landscape so it stays in the top-right corner on any screen size. -->
    <svg class="sun" viewBox="-100 -100 200 200" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="forest-halo">
          <stop offset="0" style="stop-color: var(--forest-sun); stop-opacity: 0.5" />
          <stop offset="1" style="stop-color: var(--forest-sun); stop-opacity: 0" />
        </radialGradient>
      </defs>
      <circle r="100" fill="url(#forest-halo)" />
      <circle class="sun-disc" r="45" />
    </svg>

    <svg
      class="landscape"
      viewBox="0 0 1920 1080"
      preserveAspectRatio="xMidYMax slice"
      xmlns="http://www.w3.org/2000/svg"
    >
      <defs>
        <symbol id="forest-pine" viewBox="0 0 40 100">
          <rect x="17" y="84" width="6" height="16" />
          <polygon points="20,0 36,50 4,50" />
          <polygon points="20,30 40,88 0,88" />
        </symbol>

        <!-- Canopy color comes from --canopy, set on each <use>. -->
        <symbol id="forest-round-tree" viewBox="0 0 100 140">
          <rect class="trunk" x="44" y="80" width="12" height="60" />
          <circle class="canopy" cx="50" cy="50" r="50" />
        </symbol>
      </defs>

      <path class="hills" d="M0 640 C 400 560 800 600 1100 580 S 1650 560 1920 610 V1080 H0 Z" />

      <g class="pines">
        <use
          v-for="(p, i) in pines"
          :key="i"
          href="#forest-pine"
          :x="p.x"
          :y="760 - p.h"
          :width="p.h * 0.4"
          :height="p.h"
        />
      </g>

      <path class="ground" d="M0 820 C 500 740 1300 760 1920 800 V1080 H0 Z" />

      <use
        v-for="(t, i) in trees"
        :key="i"
        href="#forest-round-tree"
        :x="t.x"
        :y="t.y - t.size * 1.4"
        :width="t.size"
        :height="t.size * 1.4"
        :style="{ '--canopy': `var(--forest-canopy-${t.kind})` }"
      />
    </svg>
  </div>
</template>

<script lang="ts">
type CanopyKind = 'pink' | 'orange'

export default {
  name: 'ForestBackground',
  data() {
    // A fixed pattern rather than Math.random(), so the scene is the same on every visit.
    const pineHeights = [150, 190, 130, 170]

    return {
      pines: Array.from({ length: 26 }, (_, i) => ({
        x: i * 76 - 20,
        h: pineHeights[i % pineHeights.length]!,
      })),
      trees: [
        { x: 140, y: 880, size: 170, kind: 'pink' },
        { x: 560, y: 830, size: 130, kind: 'orange' },
        { x: 1250, y: 830, size: 140, kind: 'pink' },
        { x: 1640, y: 870, size: 180, kind: 'orange' },
      ] as { x: number; y: number; size: number; kind: CanopyKind }[],
    }
  },
}
</script>

<style scoped>
.forest {
  overflow: hidden;
  background: linear-gradient(var(--forest-sky-top), var(--forest-sky-bottom) 60%);
}

.forest :is(path, rect, circle, polygon, stop) {
  transition:
    fill var(--theme-transition-duration) ease,
    stop-color var(--theme-transition-duration) ease;
}

.sun {
  position: absolute;
  /* Anchored from the bottom so it clears the header, which grows on small screens. */
  bottom: 50%;
  right: 2vw;
  width: clamp(180px, 22vw, 360px);
}

.sun-disc {
  fill: var(--forest-sun);
}

.landscape {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.hills {
  fill: var(--forest-hills);
}

.pines {
  fill: var(--forest-pine);
}

.ground {
  fill: var(--forest-ground);
}

.trunk {
  fill: var(--forest-trunk);
}

.canopy {
  fill: var(--canopy);
}
</style>
