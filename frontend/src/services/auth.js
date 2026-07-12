// src/services/auth.js

import api from "./api";

// sending login data to backend 
export function login(data) {
    return api.post("/login", data);
}

// sending student data to backend 
export function studentRegister(data){
    return api.post("/student/register",data)
}

// sending company data to backend 
export function companyRegister(data){
    return api.post("/company/register",data)
}










