INFILES = $(wildcard pictures/*.jpg) 
OUTFILES = $(subst pictures,thumbs, $(INFILES))
#this could also be produced by a combo of find + sed
#FILES = $(shell  find pictures -type f -iname "*.jpg" | sed 's/pictures/thumbs/g')
CONVERT_CMD = convert -thumbnail 100 $< $@
MSG = @echo "\nUpdating thumbsnail" $@

#.PHONY: all
all : $(OUTFILES)

thumbs/%.jpg: pictures/%.jpg
	$(MSG)
	$(CONVERT_CMD)

clean:
	@echo Cleaning up files..
	rm -rf thumbs/*.jpg