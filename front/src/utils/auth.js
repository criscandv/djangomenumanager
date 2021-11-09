const TOKEN_KEY = 'jwtToken'

export function saveAuthToken(value) {
    localStorage.setItem(TOKEN_KEY, value);
}

export function getAuthToken() {
    // return localStorage.getItem(TOKEN_KEY);
    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjM2MzMxMDY1LCJlbWFpbCI6IiJ9.HsZ9KtfLZivG7w5YXAKdd_YXPphxHgoVzp65O6S7EDs'
}