/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tfunada;

import au.com.bytecode.opencsv.CSVReader;
import com.google.common.collect.ArrayListMultimap;
import com.google.common.collect.ImmutableSortedMap;
import com.google.common.collect.ListMultimap;
import com.google.common.collect.Multimap;
import com.google.common.collect.Ordering;
import static com.google.common.io.Files.map;
import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

/**
 *
 * @author Neel Shah
 * MIT License under copyright act 2009.
 * Copy and use are not allowed without permission.
 * Contact: neelknightme@gmail.com
 */
public class Tfunada {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        Map<String, Integer> my_collection = new HashMap<>();
        Mydatast ds1 = new Mydatast();
        Mydatast ds2 = new Mydatast();
        Mydatast ds3 = new Mydatast();
        Mydatast ds4 = new Mydatast();
        Mydatast ds5 = new Mydatast();
        
        ArrayList<String> list = new ArrayList<>();
        try (
            Reader reader = Files.newBufferedReader(Paths.get("/home/neel/NetBeansProjects/tfunada/src/tfunada/docTweet.csv"));
            CSVReader csvReader = new CSVReader(reader);
            ){
                String[] nextRecord;
                while ((nextRecord = csvReader.readNext()) != null) {
                    String patternStr = "(?:\\s|\\A)[@]+([A-Za-z0-9-_]+)";
                                                    Pattern pattern = Pattern.compile(patternStr);
                                                    Matcher matcher = pattern.matcher(nextRecord[1]);
                                                    String result = "";
                                                    while (matcher.find()) {
                                                    result = matcher.group();
                                                    result = result.replace(" ", "");
                                                    list.add(result);
                                                    if(result.equals("@CMA_Docs"))
                                                    {
                                                        ds1.add_data(result, nextRecord[1]);
                                                    }
                                                    if(result.equals("@DocSandyB"))
                                                    {
                                                        ds2.add_data(result,nextRecord[1]);
                                                    }
                                                    if(result.equals("@drgigiosler"))
                                                    {
                                                        ds3.add_data(result,nextRecord[1]);
                                                    }
                                                    if(result.equals("@PEAKMD"))
                                                    {
                                                        ds4.add_data(result,nextRecord[1]);
                                                    }
                                                    if(result.equals("@Kapur_AK"))
                                                    {
                                                        ds5.add_data(result,nextRecord[1].replace(",", ""));
                                                    }
                                                    

                                                }

                                    }   
	}
        
        Map<String, Long> map = list.stream().collect(Collectors.groupingBy(w -> w, Collectors.counting()));
        List<Map.Entry<String, Long>> result_collection = map.entrySet().stream().sorted(Map.Entry.comparingByValue(Comparator.reverseOrder())).limit(5).collect(Collectors.toList());
        System.out.println("Top 5 users: "+result_collection);
        //ds5.search_data_key("@Kapur_AK");
        //ds5.search_data_key("@Kapur_AK");
        System.out.println("----------------");
        ds5.add_data("@Kapur_AK", "testing");
        ds5.search_data_key("@Kapur_AK");
        System.out.println("----------------");
        ds5.delete_data("@Kapur_AK", "@jblackmerMD @alandrummond2 @PEAKMD @larsendarren @Kapur_AK Thanks for your congrats @jblackmerMD ! I too look so f… https://t.co/eKyk7dd5vM");
        System.out.println("----------------");
        ds5.search_data_key("@Kapur_AK");
        System.out.println("----------------");
        //ds5.delete_all("@Kapur_AK");
        //ds5.search_data_key("@@Kapur_AK");
        
    }
   
    public static class Mydatast
    {
     ListMultimap<String, String> store_data;

     public Mydatast()
     {
       store_data = ArrayListMultimap.create();
       //System.out.println("At contructor");
     }

     void add_data(String key, String text)
     {
       store_data.put(key, text);
       //System.out.println("Added Tweet"+key);
     }

     void delete_data(String key, String text)
     {
       store_data.remove(key, text);
       System.out.println("Deleted tweet: "+text);
     }

     void search_data_key(String key)
     {
       List<String> list = store_data.get(key);
       System.out.println(list);
     }
     
     void delete_all(String key)
     {
         store_data.removeAll(key);
     }

  }
    
}

