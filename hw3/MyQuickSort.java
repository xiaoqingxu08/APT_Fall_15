public class MyQuickSort<T> {
     
    private T array[];
    private int length;
 
    public void sort(T[] inputArr, LessComp comp) {
         
        if (inputArr == null || inputArr.length == 0) {
            return;
        }
        this.array = inputArr;
        length = inputArr.length;
        quickSort(0, length - 1, comp);
    }
 
    private void quickSort(int lowerIndex, int higherIndex, LessComp comp) {
         
        int i = lowerIndex;
        int j = higherIndex;
        // calculate pivot number, I am taking pivot as middle index number
        T pivot = array[lowerIndex+(higherIndex-lowerIndex)/2];
        // Divide into two arrays
        while (i <= j) {
            /**
             * In each iteration, we will identify a number from left side which
             * is greater then the pivot value, and also we will identify a number
             * from right side which is less then the pivot value. Once the search
             * is done, then we exchange both numbers.
             */
            //while (array[i] < pivot) {
            while (comp.comp(array[i], pivot)) {
                i++;
            }
            //while (array[j] > pivot) {
            while (comp.comp(array[j], pivot)) {
                j--;
            }
            if (i <= j) {
                exchangeNumbers(i, j);
                //move index to next position on both sides
                i++;
                j--;
            }
        }
        // call quickSort() method recursively
        if (lowerIndex < j)
            quickSort(lowerIndex, j, comp);
        if (i < higherIndex)
            quickSort(i, higherIndex, comp);
    }
 
    private void exchangeNumbers(int i, int j) {
        T temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
     
    public static void main(String a[]){
         
        MyQuickSort<int> sorter = new MyQuickSort<>();
        int[] input = {24,2,45,20,56,75,2,56,99,53,12};
        LessComp comp = new LessComp();
        sorter.sort(input,comp);
        for(int i:input){
            System.out.print(i);
            System.out.print(" ");
        }
    }
}
