export CLASSPATH=".:/usr/lib/antlr-4.9-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/usr/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'