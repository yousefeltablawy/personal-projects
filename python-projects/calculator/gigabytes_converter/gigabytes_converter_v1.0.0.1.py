# Get user input for gigabytes and call conversion function.
# .احصل على إدخال المستخدم للجيجا بايت واستدعاء وظيفة التحويل
def main():
    
    # Prompt for GB input.
    # .اطلب إدخال قيمة الجيجابايت
    prompt = int(input("Enter the GB number: "))

    # Call function for conversion.
    # .استدعاء وظيفة التحويل
    output = bytes_converter(prompt)
    
    if output is not False:    # Check for errors. # .تحقق من وجود أخطاء
        print(f"{output:,}")    # Print result if successful. # .اطبع النتيجة في حال نجاح التحويل


# Convert gigabytes to bytes and handling errors.
# .تحويل الجيجابايت إلى بايت ومعالجة الأخطاء
def bytes_converter(prompt):
    
    if prompt <= 0:    # Check for invalid input. # .تحقق من إدخال المستخدم
        print("Error: \"Conversion from zero or negative gigabytes is not allowed\"")
        return False    # Signal error. # .إشارة الخطأ
    else:
        # Reset prompt to 0.
        # .أعد تعيين إدخال المستخدم إلى 0
        prompt = 0

        # Add 1 billion to prompt (assumes conversion logic).
        # .أضف مليار إلى إدخال المستخدم (يفترض منطق التحويل)
        b = prompt + 1000000000
        return b    # Return the conversion result. # .أعد القيمة المحولة
    

# Call the main function to execute the program.
# .استدعاء الفنكشن الأساسية لتنفيذ البرنامج
main()