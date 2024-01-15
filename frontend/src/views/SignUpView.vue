<template>
    <div class="container fullpage d-flex flex-grow-1">
        <div class="col-md-5 col m-auto">
            <h1 class="h2 mb-3">Registrieren</h1>
            <form @submit.prevent="register" :class="{'was-validated': needsValidation}" class="needs-validation" novalidate>
                <div class="mb-3">
                    <label class="form-label" for="usernameSignUp">Username *</label>
                    <input class="form-control" id="usernameSignUp" type="text" required v-model="user.username" placeholder="maxmustermann" />
                    <div class="invalid-feedback">
                        Username muss befüllt sein.
                    </div>
                </div>
                <div class="mb-3">
                    <label class="form-label" for="emailSignUp">Email *</label>
                    <input class="form-control" id="emailSignUp" type="email" required v-model="user.email" placeholder="max.mustermann@gmail.com" />
                    <div class="invalid-feedback">
                        Bitte gib eine gültige E-Mail Adresse ein.
                    </div>
                </div>
                <div class="mb-3">
                    <label class="form-label" for="passwordSignUp">Passwort *</label>
                    <input class="form-control" id="passwordSignUp" type="password" required v-model="user.password"/>
                    <div class="invalid-feedback">
                        Passwort muss befüllt sein.
                    </div>
                </div>
                <button class="btn btn-primary" type="submit">Registrieren</button>
                <div class="mt-1 text-danger">{{errorMessage}}</div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import userService from '../services/user.service.js'
import router from '../router/index.js'
const user = ref({
    username: '',
    email: '',
    password: ''
})
const errorMessage = ref('')
const needsValidation = ref(false)
function isEmailValid(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

async function register(){
    needsValidation.value = true
    if (!user.value.username || !user.value.email || !user.value.password) {
        errorMessage.value = "Bitte fülle alle Felder aus.";
        return
    }

    if (!isEmailValid(user.value.email)) {
        errorMessage.value = "Bitte gib eine gültige E-Mail Adresse ein.";
        return;
    }
    try {
        const response = await userService.register(user.value)
        
        if (response == 200) {
            router.push({name: 'signIn'});
        }       
    } catch(error) {
        errorMessage.value = "E-Mail oder Username existiert bereits!"
    }
}
</script>