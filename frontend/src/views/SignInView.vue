<template>
    <div class="container fullpage d-flex flex-grow-1">
        <div class="col-md-5 col m-auto">
            <h1 class="h2 mb-3">Anmelden</h1>
            <form @submit.prevent>
                <div class="mb-3">
                    <label class="form-label" for="username">Username</label>
                    <input class="form-control" id="username" type="text" placeholder="Username" />
                </div>
                <div class="mb-3">
                    <label class="form-label" for="password">Passwort</label>
                    <input class="form-control" id="password" type="password" placeholder="Passwort" />
                </div>
                <RouterLink :to="{ name: 'home' }">
                    <button @click="store.loggedIn = true" class="btn btn-primary" type="button">Anmelden</button>
                </RouterLink>
            </form>
        </div>
    </div>
</template>

<script setup>

import { RouterLink, RouterView } from 'vue-router'
import {useStore} from '../stores/store'

const store = useStore()
</script>