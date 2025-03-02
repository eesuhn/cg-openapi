generate:
	./openapi.sh generate

clean:
	./openapi.sh clean

re:
	./openapi.sh clean
	./openapi.sh generate

.PHONY: generate clean
