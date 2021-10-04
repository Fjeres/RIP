import axios from "axios";


export function apiTaskAll(){
    return axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/all/',
    })
}


export function apiTaskDelete(id){
    return axios({
        method: 'DElETE',
        url: `http://127.0.0.1:8000/api/delete/${id}`,
    })
}

export function apiTaskAdd(name, checked){
    return axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/api/add`,
        data: {
            name: name,
            checked: checked
        }
    })
}

export function apiTaskRename(id,name,checked){
    return axios({
        method: 'PUT',
        url: `http://127.0.0.1:8000/api/update/${id}`,
        data: {
            name: name,
            checked: checked
        }
    })
}

export function apiTaskCheck(id,checked){
    return axios({
        method: 'PUT',
        url: `http://127.0.0.1:8000/api/check/${id}`,
        data: {
            checked: checked
        }
    })
}