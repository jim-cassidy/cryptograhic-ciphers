class feistel{  

    public static void split(String in[])
{
    
    System.out.println(in[0]);
    return;
}


public static String replace(String str, int index, char replace){     
    if(str==null){
        return str;
    }else if(index<0 || index>=str.length()){
        return str;
    }
    char[] chars = str.toCharArray();
    chars[index] = replace;
    return String.valueOf(chars);       
}


    public static void main(String args[]){  
     System.out.println("Hello Java");  
   
    char key = 'a';
    int count = 0;
    char a1 = 'z';
    char a2 = 'z';
    char a3 = 'z';
    int b1=0, b2=0, b3=0;

    String ciphertext = new String("test");
    

    for ( int x = 0; x < 3; x++ )
    {
    a1 = ciphertext.charAt(count);
    a2 = ciphertext.charAt(count + 1);  
    b1 = a1;
    b2 = a2; 
    b3 = a1 ^ key;    
    a1 = a2;
    a2 = (char)b3; 
    ciphertext = replace(ciphertext,x,a1);
    ciphertext = replace(ciphertext,x+1,a2);
    System.out.println(ciphertext);   
    }

  
   


    }  
}  
