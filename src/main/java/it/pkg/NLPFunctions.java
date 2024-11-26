/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package it.pkg;

import io.trino.spi.function.Description;
import io.trino.spi.function.ScalarFunction;
import io.trino.spi.function.SqlType;
import io.trino.spi.type.StandardTypes;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class NLPFunctions
{
    private NLPFunctions()
    {
        throw new UnsupportedOperationException("This is a utility class and cannot be instantiated");
    }

    @ScalarFunction("square")
    @Description("Returns the square of a number")
    @SqlType("double")
    public static double square(@SqlType("double") double value)
    {
        return value * value;
    }

    @ScalarFunction("run_py")
    @Description("Runs the Python Script")
    @SqlType(StandardTypes.VARCHAR)
    public static void run_py(@SqlType(StandardTypes.VARCHAR) String scriptPath)
    {
        try {
            // Arguments to the script (if any)
            String[] command = {"python3", scriptPath};

            // Create a ProcessBuilder
            ProcessBuilder processBuilder = new ProcessBuilder(command);

            // Start the process
            Process process = processBuilder.start();

            // Read the output of the Python script
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Read any errors
            BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            while ((line = errorReader.readLine()) != null) {
                System.err.println(line);
            }

            // Wait for the process to complete
            int exitCode = process.waitFor();
            System.out.println("Python script exited with code: " + exitCode);
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}
