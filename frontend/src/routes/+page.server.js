export function load({ cookies }) {
	const csrftoken = cookies.get('csrftoken');
    cookies.set('csrfToken', csrftoken, { path : '/'})

	return {
		csrfToken: csrftoken;
	};
}