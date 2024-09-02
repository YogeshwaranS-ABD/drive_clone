import sqlite3 as sql

def decrypt(password):
	e_pass=''
	for i in password:
		e_pass+=chr(ord(i)-7)
	return e_pass

def user_check(username, password):
	conn = sql.connect('./static/flexi.db')
	cur = conn.cursor()
	users = cur.execute('select username, password from users where username="{username}"')
	users = users.fetchall()
	if len(users)==0:
		return "The username is not registered with our records. Please Sign Up to use the service."
	elif users[0][1]!=decrypt(password):
		return "The password you enterd was incorrect. Try again"
	else:
		return 1

why = {
	1: ["Smart Storage with Advanced Compression","Maximize your storage efficiency! Flexi Cloud uses cutting-edge compression technology to shrink your file sizes, enabling you to store more data without compromising quality. Enjoy reduced storage costs and a more organized cloud environment."],

	2: ["Rapid File Access","Get your files in a flash. Our sophisticated decompression technology ensures that your data is quickly and efficiently delivered to you. What’s compressed in the cloud is effortlessly decompressed on our servers, so you can access your files instantly."],

	3: ["Top-Notch Security","Protecting your data is our priority. With Amazon S3’s secure infrastructure combined with our advanced encryption methods, Flexi Cloud keeps your files safe from unauthorized access while maintaining their integrity."],

	4: ["Scalable and Reliable","From small projects to large-scale enterprises, Flexi Cloud scales to meet your needs. Count on us for reliable performance and consistent service, no matter the size of your data."],
	
	5: ["Seamless Integration","Flexi Cloud integrates effortlessly with your existing systems and applications. Our user-friendly API and comprehensive support documentation make setup and integration smooth and straightforward."],
}