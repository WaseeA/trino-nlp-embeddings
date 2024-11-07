package it.pkg;

import java.util.Set;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableSet;

import io.trino.spi.Plugin;
import io.trino.spi.connector.ConnectorFactory;

public class NLPPlugin implements Plugin {

    @Override
    public Iterable<ConnectorFactory> getConnectorFactories()
    {
        return ImmutableList.of(new NLPConnectorFactory());
    }

    @Override
    public Set<Class<?>> getFunctions() 
    {
        return ImmutableSet.of(NLPFunctions.class);
    }
}
