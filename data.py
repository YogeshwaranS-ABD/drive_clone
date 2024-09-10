import sqlite3 as sql

def encrypt(password):
	e_pass=''
	for i in password:
		e_pass+=chr(ord(i)+7)
	return e_pass

def decrypt(password):
	e_pass=''
	for i in password:
		e_pass+=chr(ord(i)-7)
	return e_pass

def update_db(data): # data = [username, email, password-encrypted]
	with sql.connect('./static/flexi.db') as conn:
		cur = conn.cursor()
		cur.execute(f'insert into users values("{data[0]}","{data[1]}","{data[2]}","{data[3]}")')
		cur.close()

def is_unique_user(user,email):
	with sql.connect('./static/flexi.db') as conn:
		cur = conn.cursor()
		data = cur.execute(f'select username, email from users where username="{user}" or email="{email}"')
		data = data.fetchall()
		cur.close()
		if len(data)!=0:
			return 0
		else:
			return 1

def user_check(username, password):
	conn = sql.connect('./static/flexi.db')
	cur = conn.cursor()
	users = cur.execute(f'select username, password, fullname from users where username="{username}"')
	users = users.fetchall()
	cur.close()
	conn.close()
	if len(users)==0:
		return "The username is not registered with our records. Please Sign Up to use the service."
	elif users[0][1]!=encrypt(password):
		return "The password you enterd was incorrect. Try again"
	else:
		return [1, users[0][-1].split()[0], users[0][0]]

why = {
	1: ["Smart Storage with Advanced Compression","Maximize your storage efficiency! Flexi Cloud uses cutting-edge compression technology to shrink your file sizes, enabling you to store more data without compromising quality. Enjoy reduced storage costs and a more organized cloud environment."],

	2: ["Rapid File Access","Get your files in a flash. Our sophisticated decompression technology ensures that your data is quickly and efficiently delivered to you. What’s compressed in the cloud is effortlessly decompressed on our servers, so you can access your files instantly."],

	3: ["Top-Notch Security","Protecting your data is our priority. With Amazon S3’s secure infrastructure combined with our advanced encryption methods, Flexi Cloud keeps your files safe from unauthorized access while maintaining their integrity."],

	4: ["Scalable and Reliable","From small projects to large-scale enterprises, Flexi Cloud scales to meet your needs. Count on us for reliable performance and consistent service, no matter the size of your data."],
	
	5: ["Seamless Integration","Flexi Cloud integrates effortlessly with your existing systems and applications. Our user-friendly API and comprehensive support documentation make setup and integration smooth and straightforward."],
}