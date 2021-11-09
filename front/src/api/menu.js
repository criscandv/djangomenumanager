import http from "../utils/http";

export async function getMenus(name=""){
    let url = 'menus/';

    if(name){
        url = `${url}?name=${name}`
    }

    const response = await http.get(url)
    return response.data
}