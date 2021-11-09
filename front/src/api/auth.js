import http from "../utils/http";

export async function login({username='', password=''}){
    let response = await http.post('auth/', {username, password})
    return response.data
}