public class Clone752AllCodeParts { 
public static void main (String [] args) throws Exception { 
     ObservableList < Integer > olist = new ObservableList < > (); 
     olist.getObservable ().subscribe (System.out :: println); 
     olist.add (1); 
     Thread.sleep (1000); 
     olist.add (2); 
     Thread.sleep (1000); 
     olist.add (3); 
 } 
 
public static void main (String [] args) {
List<Integer> initialNumbers=new ArrayList<Integer>();
initialNumbers.add(1);
initialNumbers.add(2);
Observable<Integer> observableInitial=Observable.from(initialNumbers);
ReplaySubject<Integer> subject=ReplaySubject.create();
Observable<Integer> source=Observable.merge(observableInitial,subject);
source.subscribe(null);
for([int i=0] i < 100 [++i])
subject.onNext(i);
}

}