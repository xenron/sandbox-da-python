/*
 *Regular JSON
 */
{ authorname: 'Chad Adams' }


/*
 * JSONP
 */
callback({ authorname: 'Chad Adams' });


/*
 * Using JSONP in JavaScript
 */
callback = function (data) {
    alert(data.authorname);
};