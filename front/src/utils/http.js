import axios from 'axios'
import { getAuthToken } from './auth'

const http = axios.create({
    baseURL: 'http://localhost:8000/api/',
    headers: {'Content-Type': 'application/json'},
});

http.interceptors.request.use(
    function (config){
        const token = getAuthToken();
        if(token){
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    function(err){
        return Promise.reject(err)
    }
)

export default http;