export async function getCsrfToken() {
    const res = await fetch("/api/get-csrf-token/");
    if (res.status === 200) {
        const data = await res.json();
        setCookie("csrftoken", data.csrfToken);
    } else {
        console.error("Unable to retrieve CSRF token from backend");
    }
    
}

export function getCookie(name: string): any {
    const cookies = document.cookie.split("; ");
    for (let cookie of cookies) {
        if (cookie.startsWith(name)) {
            return cookie.split("=")[1];
        }
    }
    return null;
}

export function setCookie(name: string, value: string, exdays?: number) {
    let cookie = name + "=" + value + ";"
    if (exdays) {
        const d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        const expires = "expires=" + d.toUTCString() + ";";
        cookie += expires;
    }
    document.cookie = cookie;
}