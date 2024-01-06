<template>
    <div class="container fullpage d-flex flex-grow-1">
        <div class="col-md-5 col m-auto">
            <h1 class="h2 mb-3">Registrieren</h1>
            <form @submit.prevent>
                <div class="mb-3">
                    <label class="form-label" for="usernameSignUp">Username</label>
                    <input class="form-control" id="usernameSignUp" type="text" placeholder="Username" />
                </div>
                <div class="mb-3">
                    <label class="form-label" for="emailSignUp">Email</label>
                    <input class="form-control" id="emailSignUp" type="email" placeholder="Username" />
                </div>
                <div class="mb-3">
                    <label class="form-label" for="passwordSignUp">Passwort</label>
                    <input class="form-control" id="passwordSignUp" type="password" placeholder="Passwort" />
                </div>
                <RouterLink :to="{ name: 'signIn' }">
                    <button class="btn btn-primary" type="submit">Registrieren</button>
                </RouterLink>
            </form>
        </div>
    </div>
</template>

<script setup>
</script>