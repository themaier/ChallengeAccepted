<template>
  <div>
    <div class="container-md">
      <h1 class="my-4">Freunde</h1>
    </div>
    <div class="container-md bg-body-secondary py-3 rounded">
      <h2 class="mb-4">Freunde hinzufügen</h2>
      <form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      </form>
      <div class="container-md bg-body-tertiary rounded py-2">
        <ul class="px-0 my-0">
          <li class="row align-items-center py-3 gy-2 gy-lg-0">
            <div class="col-lg-2">Max Wenzinger</div>
            <div class="col-3 col-lg align-self-end d-flex  justify-content-lg-end d-flex-column">
              <button class="btn btn-success btn-block">Hinzufügen</button>
            </div>
          </li>
          <li class="row align-items-center py-3 gy-2 gy-lg-0">
            <div class="col-lg-2">Sepp Schneewasser</div>
            <div class="col-3 col-lg align-self-end d-flex  justify-content-lg-end d-flex-column">
              <button class="btn btn-success">Hinzufügen</button>
            </div>
          </li>
        </ul>
      </div>
    </div>
    <div class="container-md bg-body-secondary py-3 rounded mt-4">
      <h2 class="mb-4">Meine Freunde</h2>
      <div class="container-md bg-body-tertiary rounded py-2">
        <ul class="px-0 my-0">
          <li class="row align-items-center py-3 gy-2 gy-lg-0">
            <RouterLink :to="{ name: 'home' }" class="col-lg-2 link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">Tobias Maier</RouterLink>
            <div class="col-3 col-lg align-self-end d-flex  justify-content-lg-end d-flex-column">
              <button class="btn btn-danger">Entfernen</button>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>