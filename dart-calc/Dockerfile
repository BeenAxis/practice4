FROM google/dart
COPY . /app
WORKDIR /app
RUN dart compile exe calc.dart
CMD ["./calc.exe"]