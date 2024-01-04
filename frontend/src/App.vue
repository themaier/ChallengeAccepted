
<template>
  <header>
      <nav class="navbar bg-dark navbar-expand-lg" data-bs-theme="dark">
        <div class="container-fluid">
          <RouterLink class="navbar-brand" to="#">Challenge accepted</RouterLink>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                <li class="nav-item" v-if="store.loggedIn">
                  <RouterLink class="nav-link active" aria-current="page" to="#">Meine Challenges</RouterLink>
                </li>
                <li class="nav-item" v-if="store.loggedIn">
                  <RouterLink class="nav-link" to="#">Trending</RouterLink>
                </li>
                <li class="nav-item" v-if="store.loggedIn">
                  <RouterLink class="nav-link" to="#">Challenge erstellen</RouterLink>
                </li>
                <li class="nav-item" v-if="store.loggedIn">
                  <RouterLink class="nav-link" to="#">Profil</RouterLink>
                </li>
                <li class="nav-item" v-if="!store.loggedIn">
                  <RouterLink class="btn btn-primary ms-lg-2 mt-2 mt-lg-0" to="/registrieren">Registrieren</RouterLink>
                </li>
                <li class="nav-item" v-if="!store.loggedIn">
                  <RouterLink class="btn btn-outline-primary ms-lg-2 mt-2 mt-lg-0" to="/anmelden">Anmelden</RouterLink>
                </li>
                <li class="nav-item" v-if="store.loggedIn">
                  <RouterLink :to="{ name: 'signIn' }">
                    <button @click="store.loggedIn = false" class="btn btn-danger ms-lg-2 mt-2 mt-lg-0">Abmelden</button>
                  </RouterLink>
                </li>
              </ul>
            </div>
        </div>
      </nav>
  </header>

  <main>
    <RouterView />
  </main>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import {useStore} from './stores/store'

const store = useStore()
</script>