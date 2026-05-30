data = input("File type : ").strip().lower()

if not data.__contains__("."):
	print("application/octet-stream")
	exit(0)

ind = data.rfind(".")
file_type = data[ind:len(data)]


match file_type:
	case ".gif" | ".png" | ".jpeg":
		print("image/"+file_type[1:])
	case ".jpg":
		print("image/jpeg")
	case ".txt":
		print("text/plain")
	case ".pdf" | ".zip":
		print("application/"+file_type[1:])
	case _:
		print("application/octet-stream")
