reviewed = (
	(0.5321100917431193, 'Check true statements about Activity.onSaveInstanceState(Bundle)', 'Check true statements (if any) about Fragment'),
	(0.609375, 'Check true statements about Activity.onSaveInstanceState(Bundle)', 'Choose true statements about method Fragment.setRetainInstance()'),
	(0.6923076923076923, 'Check true statements about Activity.onSaveInstanceState(Bundle)', 'Check true statements about ListActivity'),
	(0.5072463768115942, 'Check true statements about Activity.onSaveInstanceState(Bundle)', 'Which of the following are true statements about LayoutInfalater.inflate()'),
	(0.6078431372549019, 'Check true statements about Activity.onSaveInstanceState(Bundle)', 'Check true statements about RadioGroup'),
	(0.5901639344262295, 'Check true statements about Activity.onSaveInstanceState(Bundle)', 'Check true statements about a broadcast receiver priority.'),
	(0.5314685314685315, 'Check true statements about Activity.onSaveInstanceState(Bundle)', 'Check true statements about normal broadcasts (sent with Context.sendBroadcast)'),
	(0.6274509803921569, 'Check true statements about Activity.onSaveInstanceState(Bundle)', 'Check true statements about a Service.'),
	(0.7228915662650602, 'Check true statements (if any) about Fragment', 'Check true statements about a Service.'),
	(0.6078431372549019, 'Choose true statements about method Fragment.setRetainInstance()', 'Check true statements about a Service.'),
	(0.7692307692307693, 'Check true statements about ListActivity', 'Check true statements about a Service.'),
	(0.5178571428571429, 'Which of the following are true statements about LayoutInfalater.inflate()', 'Check true statements about a Service.'),
	(0.7894736842105263, 'Check true statements about RadioGroup', 'Check true statements about a Service.'),
	(0.711864406779661, 'Check true statements', 'Check true statements about a Service.'),
	(0.5043478260869565, 'Which of the following are true statements about AlertDialog. Dialog can show', 'Check true statements about a Service.'),
	(0.7083333333333334, 'Check true statements about a broadcast receiver priority.', 'Check true statements about a Service.'),
	(0.5068493150684932, '(True or False) You can broadcast within an app.', '(True or False) You can use LayoutInflater with an XmlPullParser over a plain XML file at runtime.'),
	(0.5470085470085471, 'Check true statements about normal broadcasts (sent with Context.sendBroadcast)', 'Check true statements about a Service.'),
	(0.5079365079365079, 'Check true statements about ordered broadcasts (sent with Context.sendOrderedBroadcast) ', 'Check true statements about a Service.'),
	(0.5255474452554745, '(True or False) You can call start() again on the MediaPlayer once you have called stop()', '(True or False) You can broadcast within an app.'),
	(0.5504587155963303, 'The uniqueness of your application defined by', 'Which components of an application can be activated by intents. '),
	(0.5645161290322581, 'Which components of an application can be activated by intents. ', 'Components of different applications run in the same process'),
	(0.5660377358490566, 'You can set a Fragment tag by', 'You can apply a theme to'),
	(0.5247524752475248, '(True or False) The SQLite Open Helper caches database instances after they\xe2\x80\x99ve been successfully opened.', '(True or False) SQLiteOpenHelper.onCreate method is called only when the database does not exist'),
	(0.5970149253731343, 'Android UI toolkit is thread-safe', 'A Cursor object is not thread safe'),
	(0.5308056872037915, '(True or False) Method boolean View.post(Runnable) returns true if the Runnable was successfully executed', '(True or False) The SQLite Open Helper caches database instances after they\xe2\x80\x99ve been successfully opened.'),
	(0.5529411764705883, '(True or False) Starting with API 11 (Android 3.0) AsyncTasks can operate in parallel.', '(True or False)  SQLite database in Android is running as a separate ongoing process'),
	(0.5121951219512195, 'Broadcast access permissions can be enforced by', 'Database queries can be returned as'),
	(0.5314685314685315, "(True or False) Components in the content provider's application always have full read and write access, regardless of the specified permissions.", "(True or False) If a provider's application doesn't specify any permissions, then other applications have full access to the provider's data."),
	(0.5139664804469274, '(True or False)  SQLite database in Android is running as a separate ongoing process', '(True or False) SQLite column values are required to conform to a single type (strongly typed).'),
	(0.5193370165745856, '(True or False)  SQLite database in Android is running as a separate ongoing process', '(True or False) SQLiteDatabase.execSQL() can execute multiple statements separated by semicolons.'),
	(0.5714285714285714, 'How can you register BroadcastReceiver?', 'A BroadcastReceiver ___.'),
	(0.546875, 'Which actions will remove current Activity from the back stack?', 'Which methods allows you to receive data back from the broadcast?'),
	(0.5174825174825175, 'By default, any time spent in BroadcastReceiver.onReceive() will freeze your UI', 'Which operations are forbidden in BroadcastReceiver.onReceive()?'),
	(0.5448275862068965, '(True or False) Application with broadcast receivers can respond to broadcast events even after app has been closed or killed.', '(True or False) A Receiver registered programmatically will respond to Broadcast Intents even when the application component it is registered within is not running.'),
	(0.5082872928176796, "(True or False) Activity.onSaveInstanceState() won't be called if the user moves back in the history stack.", '(True or False) startActivityForResult() can be used with implicit Intents'),
	(0.5028571428571429, '(True or False) If an Activity want to respond to an implicit Intent it will need an <intent-filter>.', '(True or False) startActivityForResult() can be used with implicit Intents'),
	(0.5245901639344263, '(True or False) startActivityForResult() can be used with implicit Intents', '(True or False) You can broadcast within an app.'),
	(0.53125, 'Activities in the back stack can be', 'Android user interface can be'),
	(0.5581395348837209, '(True or False) In order to start an activity it has to be registered and needs <intent-filter> in AndroidManifest', '(True or False) If an Activity want to respond to an implicit Intent it will need an <intent-filter>.'),
	(0.5185185185185185, 'A stopped fragment is not visible.', 'Activity or Fragment becomes visible after call'),
	(0.5217391304347826, 'Which layout does not arrange its children in any particular manner', 'Which layouts support assigning a weight to individual children with the android:layout_weight'),
	(0.7375886524822695, 'Which attribute sets the gravity of the content of the View its used on?', 'Which attribute sets the gravity of the View or Layout in its parent?'),
	(0.6596858638743456, "_____ is the space inside the border, between the border and the actual view's content.", 'The space outside the border, between the border and the other elements next to this view are defined by'),
	(0.5467625899280576, 'All Java SE classes are available to Android programs', 'All Java features (libraries, language-syntax) are available by default in Android SDK'),
	(0.5897435897435898, 'All widgets extend View class', 'All widgets containers (layouts) extend ViewGroup'),
	(0.5426356589147286, 'Which of the following are subclasses of the ViewGroup?', 'Which of the following are true statements about LayoutInfalater.inflate()'),
	(0.5151515151515151, 'Which of the following are subclasses of the ViewGroup?', 'Which of the following are true statements about AlertDialog. Dialog can show'),
	(0.6785714285714286, 'Which of the following are subclasses of the ViewGroup?', 'Which of the following are examples of User Notification?'),
	(0.5217391304347826, 'Fragments can be used without activities', 'Fragments were introduced in '),
	(0.5409836065573771, 'Fragments can be used without activities', 'Fragments inside the host Activity can be started even if the Activity is stopped '),
	(0.5274725274725275, 'Fragments can be used without activities', 'A handler can be associated with a multiple threads'),
	(0.5538461538461539, 'Android operating system is based on', 'Android user interface can be'),
	(0.8809523809523809, 'The default <LinearLayout> orientation is', 'The default <RelativeLayout> orientation is'),
	(0.5142857142857142, 'By default, all child views of RelativeLayout are drawn at the', 'The default <RelativeLayout> orientation is'),
	(0.5154639175257731, 'How you can identify a fragment?', 'Only FrameLayout can be a placeholder container for your fragment'),
	(0.6229508196721312, 'How you can identify a fragment?', 'You can set a Fragment tag by'),
	(0.7435897435897436, 'Check true statements about ListActivity', 'Check true statements about RadioGroup'),
	(0.6823529411764706, 'Check true statements about ListActivity', 'Check true statements (if any) about Fragment'),
	(0.6885245901639344, 'Check true statements about ListActivity', 'Check true statements'),
	(0.5098039215686274, 'Check true statements about ListActivity', 'Choose true statements for method Fragment.setRetainInstance()'),
	(0.7152317880794702, 'Which of the following are true statements about LayoutInfalater.inflate()', 'Which of the following are true statements about AlertDialog. Dialog can show'),
	(0.5225225225225225, 'Which of the following are true statements about LayoutInfalater.inflate()', 'Inflation (LayoutInflater.inflate) is'),
	(0.6987951807228916, 'Check true statements about RadioGroup', 'Check true statements (if any) about Fragment'),
	(0.711864406779661, 'Check true statements about RadioGroup', 'Check true statements'),
	(0.5043478260869565, 'Check true statements about RadioGroup', 'Which of the following are true statements about AlertDialog. Dialog can show'),
	(0.6363636363636364, 'Check true statements (if any) about Fragment', 'Check true statements'),
	(0.5981308411214953, 'Check true statements (if any) about Fragment', 'Choose true statements for method Fragment.setRetainInstance()'),
	(0.6981132075471698, 'You can have multiple Activities in the foreground', 'Android app can run multiple processes in the foreground'),
	(0.7786259541984732, 'Which dimension unit is recommend when specifying font sizes', 'Which dimension units are recommend when specifying margins and padding'),
	(0.5225225225225225, 'Java Threads running in the same Process share', 'Application components in the same process use the same UI thread'),
	(0.5283018867924528, 'Java Threads running in the same Process share', 'Components of different applications run in the same process'),
	(0.5736434108527132, '(True or False) Starting with API 11 (Android 3.0) AsyncTasks can operate in parallel.', '(True or False) AsyncTask can be cancelled.'),
	(0.5454545454545454, "Which one of the following HTTP clients is Android's preferred HTTP client?", 'Which of the following are examples of User Notification?'),
	(0.6, 'You may use a fragment without its own UI', 'You can set a Fragment tag by'),
	(0.512, 'Application components in the same process use the same UI thread', 'Components of different applications run in the same process'),
	(0.5116279069767442, "In which of the following programming languages are Android's Native libraries typically written?", "Which one of the following HTTP clients is Android's preferred HTTP client?"),
	(0.5413533834586466, '(True or False) Android OS uses standard (Oracle) java virtual machine. ', '(True or False) ScrollView can host multiple direct children.'),
	(0.5178571428571429, 'Check true statements about Activity.onRestoreInstanceState(Bundle)', 'Check true statements (if any) about Fragment'),
	(0.6412213740458015, 'Check true statements about Activity.onRestoreInstanceState(Bundle)', 'Choose true statements about method Fragment.setRetainInstance()'),
	(0.6728971962616822, 'Check true statements about Activity.onRestoreInstanceState(Bundle)', 'Check true statements about ListActivity'),
	(0.6095238095238096, 'Check true statements about Activity.onRestoreInstanceState(Bundle)', 'Check true statements about RadioGroup'),
	(0.576, 'Check true statements about Activity.onRestoreInstanceState(Bundle)', 'Check true statements about a broadcast receiver priority.'),
	(0.5205479452054794, 'Check true statements about Activity.onRestoreInstanceState(Bundle)', 'Check true statements about normal broadcasts (sent with Context.sendBroadcast)'),
	(0.8, 'Activity becomes visible after call', 'Fragment becomes visible after call'),
	(0.56, 'Fragment becomes visible after call', 'Fragment lifecycle methods are called by'),
	(0.6238532110091743, 'Check true statements (if any) about Fragment', 'Choose true statements about method Fragment.setRetainInstance()'),
	(0.6823529411764706, 'Check true statements (if any) about Fragment', 'Check true statements about ListActivity'),
	(0.6987951807228916, 'Check true statements (if any) about Fragment', 'Check true statements about RadioGroup'),
	(0.6213592233009708, 'Check true statements (if any) about Fragment', 'Check true statements about a broadcast receiver priority.'),
	(0.532258064516129, 'Check true statements (if any) about Fragment', 'Check true statements about normal broadcasts (sent with Context.sendBroadcast)'),
	(0.5769230769230769, 'Choose true statements about method Fragment.setRetainInstance()', 'Check true statements about ListActivity'),
	(0.5217391304347826, 'Choose true statements about method Fragment.setRetainInstance()', 'Which of the following are true statements about LayoutInfalater.inflate()'),
	(0.5490196078431373, 'Choose true statements about method Fragment.setRetainInstance()', 'Check true statements about RadioGroup'),
	(0.5409836065573771, 'Choose true statements about method Fragment.setRetainInstance()', 'Check true statements about a broadcast receiver priority.'),
	(0.5594405594405595, 'Choose true statements about method Fragment.setRetainInstance()', 'Check true statements about normal broadcasts (sent with Context.sendBroadcast)'),
	(0.5263157894736842, 'Choose true statements about method Fragment.setRetainInstance()', 'Check true statements about ordered broadcasts (sent with Context.sendOrderedBroadcast) '),
	(0.7346938775510204, 'Check true statements about ListActivity', 'Check true statements about a broadcast receiver priority.'),
	(0.5546218487394958, 'Check true statements about ListActivity', 'Check true statements about normal broadcasts (sent with Context.sendBroadcast)'),
	(0.515625, 'Check true statements about ListActivity', 'Check true statements about ordered broadcasts (sent with Context.sendOrderedBroadcast) '),
	(0.6875, 'Check true statements about RadioGroup', 'Check true statements about a broadcast receiver priority.'),
	(0.5811965811965812, 'Check true statements about RadioGroup', 'Check true statements about normal broadcasts (sent with Context.sendBroadcast)'),
	(0.5396825396825397, 'Check true statements about RadioGroup', 'Check true statements about ordered broadcasts (sent with Context.sendOrderedBroadcast) '),
	(0.5316455696202531, 'Check true statements', 'Check true statements about a broadcast receiver priority.'),
	(0.5384615384615384, '(True or False) ScrollView can host multiple direct children.', '(True or False) AsyncTask can be cancelled.'),
	(0.5688073394495413, '(True or False) ScrollView can host multiple direct children.', '(True or False) You can broadcast within an app.'),
	(0.5714285714285714, '(True or False) AsyncTask can be cancelled.', '(True or False) You can broadcast within an app.'),
	(0.656934306569343, 'Check true statements about a broadcast receiver priority.', 'Check true statements about normal broadcasts (sent with Context.sendBroadcast)'),
	(0.589041095890411, 'Check true statements about a broadcast receiver priority.', 'Check true statements about ordered broadcasts (sent with Context.sendOrderedBroadcast) '),
	(0.8982035928143712, 'Check true statements about normal broadcasts (sent with Context.sendBroadcast)', 'Check true statements about ordered broadcasts (sent with Context.sendOrderedBroadcast) '),
)