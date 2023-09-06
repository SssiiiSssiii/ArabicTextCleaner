# ArabicTextCleaner
**Do What?**
* Tokenization: Breaking down Arabic text into individual words or tokens.                   
* Normalization: Standardizing text by converting characters to their base forms.
  
  | from | to |
  | -----|----|
  | أ-إ-آ | ا |
  | ى | ي |
  | ة | ه |
  | الْعَرَبِيَّة | العربية |
  | العـــربية | العربية |
* Stop Word Removal: Eliminating common and less informative words like articles and conjunctions.(**You can also review the text file containing stop words and make modifications as needed in the `src` file**)
                      
  ![Alt text](/Images/Sample_of_Arabic_stop_words.png)
           
* Stemming: Reducing words to their root forms to enhance text analysis and information retrieval. (التجذيع)
  
**These preprocessing steps are essential for enhancing the quality and usability of Arabic text data in various `NLP` and machine learning tasks.**                              
                                     

## Test
**Input**    

![Alt text](/Images/Test.png)    

**Outout**                      

![Alt text](/Images/Output.png)


## Note
**Feel free to use and contribute to this repository to advance our Arabic text processing projects. ')**         
