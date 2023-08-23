export function getCookie(name: string): string {
    const cookies = document.cookie.split("; ");
    for (let cookie of cookies) {
        if (cookie.startsWith(name)) {
            return cookie.split("=")[1];
        }
    }

    throw new Error(`Cookie with name ${name} not found.`)
}